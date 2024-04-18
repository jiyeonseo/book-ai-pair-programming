def main():
    try:
        divisor = 0
        x = 1 / divisor
    except Exception as e:
        print("Error", e)
    
    try:
        my_dict = {'name': 'Alice'}
        age = my_dict.get('age')
    except Exception as e:
        print("Error", e)

    try:
        int('abc')  # ValueError
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    main()
