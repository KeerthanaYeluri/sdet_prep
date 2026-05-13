# a=[1,2,3,4,5,7,9]
# a.sort()
# print(len(a)%2==0)
#
# if len(a)%2==0:
#     print("even.....")
# else:
#     median_position = int((len(a) - 1) / 2)
#     print(a[median_position])
#
#
#
#
#
# a=[1,2,3,4,5,7,9,10]
# a.sort()
# print(len(a)%2==0)
#
# if len(a)%2==0:
#     median_position_1 = int((len(a) - 1) / 2)
#     print(a[median_position_1])
#     median_position_2=median_position_1+1
#     print("median",(a[median_position_1]+a[median_position_2])/2)
# else:
#     median_position = int((len(a) - 1) / 2)
#     print(a[median_position])
#from pygetwindow import activate


def median_of_array(arr1, arr2):
    arr1_median = find_median(arr1)
    print(arr1_median)
    arr2_median = find_median(arr2)
    print(arr2_median)
    print("median is : ",(arr1_median+ arr2_median)/ 2)
def find_median(list_of_arrays):
    median_position_1 = int((len(list_of_arrays) - 1) / 2)
    print(median_position_1)
    if len(list_of_arrays) % 2 == 1:
        return list_of_arrays[median_position_1]
    else:
        median_position_2 = median_position_1 + 1
        return (list_of_arrays[median_position_1] + list_of_arrays[median_position_2]) / 2
a=[1,2,3,4]
b=[5,6,7,8]
median_of_array(a,b)



def find_median(a):
    a.sort()
    if len(a)%2==0:
        median_position_1=int((len(a)-1) / 2)
        median_position_2 = median_position_1 + 1
        return (a[median_position_1] + a[median_position_2]) / 2
    else:
        median_position=int((len(a)-1) / 2)
        return (a[median_position])
def median(arr1,arr2):
    arr1=find_median(arr1)
    arr2=find_median(arr2)
    return (arr1 + arr2) / 2
arr1=[1,2,3,4]
arr2=[5,6,7,8]
print(median(arr1,arr2))






a=[10,20,30,40]
length= len(a)
if length%2==1:
    mid=length//2
    print(a[mid])
else:
    mid1=length//2
    mid2=length//2-1
    median=(a[mid1] + a[mid2])/2
    print(median)


