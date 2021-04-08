'''Subdomain Visit Count

    William Ikenna-Nwosu (wiknwo)

    A website domain like "discuss.leetcode.com" consists of 
    various subdomains. At the top level, we have "com", at 
    the next level, we have "leetcode.com", and at the 
    lowest level, "discuss.leetcode.com". When we visit a 
    domain like "discuss.leetcode.com", we will also visit 
    the parent domains "leetcode.com" and "com" implicitly.

    Now, call a "count-paired domain" to be a count 
    (representing the number of visits this domain received), 
    followed by a space, followed by the address. An 
    example of a count-paired domain might be 
    "9001 discuss.leetcode.com".

    We are given a list cpdomains of count-paired domains. 
    We would like a list of count-paired domains, (in the 
    same format as the input, and in any order), that 
    explicitly counts the number of visits to each subdomain.
'''
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = {} # Dictionary mapping domains to visit counts
        # Iterate through count-paired domains
        for cpdomain in cpdomains:
            visit_count, domain = cpdomain.split(' ') # Get the visit count and the domain from the sount-pair domain
            visit_count = int(visit_count) # Convert visit count to integer
            subdomains = domain.split('.') # Get sudomain
            # Iterate through splitted domain and create subdomains
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:]) # Create the subdomains from the domain
                domain_dict[subdomain] = domain_dict.get(subdomain, 0) + visit_count # If subdomain already has a visit count, get returns it. Otherwise it is set to zero and incremented by visit_count
        return [' '.join([str(value), key]) for key, value in domain_dict.items()]
            
            