from producer import Producer
import time

def main():
    time.sleep(10)
    producer = Producer()
    producer.produce_data_loop()

if __name__ == "__main__":
    main()
        
