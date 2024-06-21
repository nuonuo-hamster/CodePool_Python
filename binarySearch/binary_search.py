# binary search
def binary_search(data, key):
    
    low = 0
    high = len(data)-1

    # if( (key < data[low]) | (key > data[high]) ):
    #     print("Out of range")
    #     return -1
    
    while (low <= high) :
        mid = int( (high+low) / 2 )
        
        if key == data[mid]:
            return mid
        
        elif key > data[mid]:
            low = mid + 1
        
        else: high = mid - 1
    
    return -1

# return entity
def locate_result(location):
    if(location == -1):
        print("can't find data")
    else: 
        print("destination is {}".format(location))
        # print(f"destination is {location}")


if __name__ == '__main__':

    # 生成列表 0~25
    interval = 26
    table = []

    for i in range(interval):
        table.append (i)

    # 整理列表
    table.sort()
    print(table)

    # 輸入查找
    search_num = input("Input number >>")
    search_num = int(search_num)

    # 輸出結果
    location = binary_search(table, search_num)
    locate_result(location)
