class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        counter = 0
        for c in range (len(students)):
            counter+=abs(students[c] - seats[c])
        return counter