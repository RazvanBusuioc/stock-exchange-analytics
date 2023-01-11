from producer import init_producer, produce_data_loop

def main():
    producer = init_producer()
    produce_data_loop(producer)
    

if __name__ == "__main__":
    main()
        
