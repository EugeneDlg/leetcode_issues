def move_zeros(nums):
    zero_pointer = -1
    zero_found = False
    for pointer in range(len(nums)):
        if nums[pointer] == 0 and not zero_found:
            zero_pointer = pointer
            zero_found = True
        elif nums[pointer] != 0 and zero_pointer > -1:
            nums[zero_pointer] = nums[pointer]
            nums[pointer] = 0
            zero_pointer += 1