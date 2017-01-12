def Binary_Search(arr, to_find):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
  """
  i = 0
  n = len(arr)
  mid = n/2
  while i < n:
    print mid
    if to_find > arr[mid]:
      mid = n-mid/2
      i+=1
    elif to_find <arr[mid]:
      mid = mid - mid/2
      i+=1
    else:
      return mid


def Bisection(func, left_side, right_side, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
  """
  pass


arr = [1,2,3,4,5,6,7,8,9]
print arr[7]
to_find = 7
#print Binary_Search(arr, to_find)