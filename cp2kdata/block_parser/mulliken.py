import regex as re
import numpy as np

MULLIKEN_RE = re.compile(
    """
    \s+Mulliken\sPopulation\sAnalysis\s*\n
    \n
    \s\#.+\n
    (
        \s+(?P<atom>\d+)
        \s+(?P<element>\w+)
        \s+(?P<kind>\d+)
        \s+(?P<alpha>[\s-]\d+\.\d+)
        \s+(?P<beta>[\s-]\d+\.\d+)
        \s+(?P<net_charge>[\s-]\d+\.\d+)
        \s+(?P<spin_moment>[\s-]\d+\.\d+)
        \n
    )+
    """,
    re.VERBOSE
)

def parse_mulliken_pop_list(output_file):
    mulliken_pop_list = []
    for match in MULLIKEN_RE.finditer(output_file):
        mulliken_pop = []
        for element, alpha, beta, net_charge, spin_moment in zip(*match.captures("element", "alpha", "beta", "net_charge", "spin_moment")):
            mulliken_pop.append(
                {
                    "element": element,
                    "alpha": float(alpha),
                    "beta": float(beta),
                    "net_charge": float(net_charge),
                    "spin_moment": float(spin_moment)
                }
            )
        mulliken_pop_list.append(mulliken_pop)
    if  mulliken_pop_list:
        return  mulliken_pop_list
    else:
        return None