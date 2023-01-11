from consumer import Consumer
from topics import topics
import time

def main():
    time.sleep(10)
    consumer = Consumer()
    consumer.subscribe(topics)
    consumer.consume_data_loop()
    

if __name__ == "__main__":
    main()
        