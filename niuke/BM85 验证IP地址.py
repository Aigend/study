# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM85 验证IP地址.py
# @Date    : 2022/07/04:22:14
# @Author  : jinwenlong@oppo.com
class Solution:

    def check_ipv4(self, IP):
        ip = IP.split(".")
        for p in ip:
            if p.startswith("0") or len(p) > 3:
                return "Neither"
            for q in p:
                if q < "0" or q > "9":
                    return "Neither"
            if int(p) > 255:
                return "Neither"
        return "IPv4"

    def check_ipv6(self, IP):
        ip = IP.split(":")
        for p in ip:
            if len(p) > 4 or not p:
                return "Neither"
            for q in p:
                if not("0"<=q<"9" or "a"<=q<="f" or "A"<=q<="F"):
                    return "Neither"
        return "IPv6"

    def solve(self, IP: str) -> str:
        # write code here
        v4 = IP.count(".")
        v6 = IP.count(":")
        if v4 == 3 and v6 == 0:
            return self.check_ipv4(IP)
        if v4 == 0 and v6 == 7:
            return self.check_ipv6(IP)
        else:
            return "Neither"

if __name__ == '__main__':
    print(Solution().solve("2001:db8:85a3:0::8a2E:0370:7334"))
