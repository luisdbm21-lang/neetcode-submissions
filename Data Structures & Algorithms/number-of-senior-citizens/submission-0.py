class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_seniors, age = 0, 0

        for i in range(len(details)):
            age = details[i][11:13]

            if int(age) > 60:
                count_seniors += 1

        return count_seniors