from consumer import Consumer
from topics import topics

def main():
    consumer = Consumer()
    consumer.subscribe(topics)
    consumer.consume_data_loop()
    

if __name__ == "__main__":
    main()
        