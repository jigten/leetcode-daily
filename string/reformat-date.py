class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        month_map = {
            "Jan": "1",
            "Feb": "2",
            "Mar": "3",
            "Apr": "4",
            "May": "5",
            "Jun": "6",
            "Jul": "7",
            "Aug": "8",
            "Sep": "9",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        return "-".join([year, month_map[month], day[:-2]])
