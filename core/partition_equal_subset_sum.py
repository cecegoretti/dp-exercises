def partition_subset(nums):

  """
    Determine whether a list of positive integers can be partitioned
    into two disjoint subsets with equal sum.

    The problem is reduced to a subset-sum decision problem:
    we check whether there exists a subset of nums whose sum equals
    half of the total sum.

    Dynamic programming approach:
    dp[i][j] is True if it is possible to obtain sum i using the
    elements nums[0..j].

    Time complexity: O(n * S)
    Space complexity: O(n * S)
    where n = len(nums) and S = total_sum // 2.
    """
  total=sum(nums)
  if total%2==1:
    return False
    #it is impossible to divide the set into two subsets with equal sum if the total amount contained in nums is an odd number
  aim_weight=total//2
  dp=[[False]*len(nums) for _ in range(aim_weight+1)]
  # dp[i][j] = True if i can obtain exactly i space filled with a subset of nums[0:j+1]
  for i in range(aim_weight+1):
    if i==0 or i==nums[0]:
      dp[i][0]=True
  #base case consist in the bag completely filled with the first object or no space left to fill
  for j in range(1,len(nums)):
    for i in range(aim_weight+1):
      if i==0:
        dp[i][j]=True #base case
      else:
        id nums[j]<=i:
          dp[i][j]=dp[i][j-1] or dp[i-nums[j]][j-1]
        else:
          dp[i][j]=dp[i][j-1]
  return dp[aim_weight][len(nums)-1]
  
