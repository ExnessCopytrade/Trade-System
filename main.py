from DataHandler import SimpleCSVHandler

# Declare the components with respective parameters
events = []
bars = SimpleCSVHandler(events, 'C:/users/hunte/repos/trade/data/EURUSD_DAILY_5YR.csv')

print(bars.bars.head(2))

bars.update_bars()
print(bars.get_latest_bars())
bars.update_bars()
bars.update_bars()
print(bars.get_latest_bars(N=3))
print()
print(events)

'''
strategy = Strategy(..)
port = Portfolio(..)
broker = ExecutionHandler(..)

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
    time.sleep(10*60)
'''
