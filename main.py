from DataHandler import HistoricCSVDataHandler
from Strategy import SimpleBuy
from Portfolio import NaivePortfolio
from ExecutionHandler import SimulatedExecutionHandler

# Declare the components with respective parameters
events = [] # event queue
symbols = ['EURUSD_1D'] # just the eurusd daily for now
bars = HistoricCSVDataHandler(events, 'C:/users/hunte/repos/trade/data/', symbols)
strategy = SimpleBuy(bars, events)
port = NaivePortfolio(bars, events, None)
broker = SimulatedExecutionHandler(events)

while True:
    # Update the bars (specific backtest code, as opposed to live trading)
    if bars.continue_backtest == True:
        bars.update_bars()
    else:
        break

    # Handle the events
    while True:
        try:
            event = events.get(False)
        except Queue.Empty:
            break
        else:
            if event is not None:
                if event.type == 'MARKET':
                    strategy.calculate_signals(event)
                    port.update_timeindex(event)

                elif event.type == 'SIGNAL':
                    port.update_signal(event)

                elif event.type == 'ORDER':
                    broker.execute_order(event)

                elif event.type == 'FILL':
                    port.update_fill(event)

    # 10-Minute heartbeat
    #time.sleep(10*60)
    break
