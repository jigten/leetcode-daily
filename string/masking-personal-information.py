class Solution:
    def _maskEmail(self, s: str) -> str:
        name, domain = s.split("@")
        return name[0].lower() + "*****" + name[-1].lower() + "@" + domain.lower()

    def _maskNumber(self, s: str) -> str:
        mapping = str.maketrans("", "", "()- +")
        num = s.translate(mapping)
        n = len(num)
        masked = ""

        if n == 10:
            masked = "***-***-"
        elif n == 11:
            masked = "+*-***-***-"
        elif n == 12:
            masked = "+**-***-***-"
        else:
            masked = "+***-***-***-"

        return masked + num[-4:]

    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            return self._maskEmail(s)
        else:
            return self._maskNumber(s)
