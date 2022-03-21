def create_a_record():
    return "test1"

def get_a_record():
    return "test2"

def delete_a_record():
    return "test3"

def main():
    print("hello")
    tester = "test3"

    choice_map = {'test1': create_a_record,
                  'test2': get_a_record,
                  'test3': delete_a_record}
    
    print(choice_map.get(tester)())

if __name__ == '__main__':
    main()