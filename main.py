from DataHandler import HistoricCSVDataHandler
from Strategy import SimpleBuy
from Strategy import BuyAndHoldStrategy
from Portfolio import NaivePortfolio
from ExecutionHandler import SimulatedExecutionHandler

# Declare the components with respective parameters
events = [] # event queue
symbols = ['EURUSD_1D'] # just the eurusd daily for now
bars = HistoricCSVDataHandler(events, 'C:/users/hunte/repos/trade/data/', symbols)
strategy = SimpleBuy(bars, events)
port = NaivePortfolio(bars, events, None, 1000)
broker = SimulatedExecutionHandler(events)

y=0
while True:
    x = port.current_holdings['total']
    print('current holdings: {:,.4f}'.format(x))
    # Update the bars (specific backtest code, as opposed to live trading)
    if bars.continue_backtest == True:
        bars.update_bars()
    else:
        break

    # Handle the events
    while True:
        event = None
        if len(events) > 0:
            event = events.pop(0)
        else:
            break
        if event is not None:
            if event.type == 'MARKET':
                strategy.calculate_signals(event)
                port.update_timeindex(event)

            elif event.type == 'SIGNAL':
                port.update_signal(event)

            elif event.type == 'ORDER':
                # ignoring commissions rn to solve the "fill_cost" debacle
                broker.execute_order(event)
                pass

            elif event.type == 'FILL':
                port.update_fill(event)

    # 10-Minute heartbeat
    #time.sleep(10*60)
    print('end of hb, latest bar: ', bars.get_latest_bars(symbols[0], N=1)[0])
    if y < 10:
        y += 1
        pass
    else:
        break
