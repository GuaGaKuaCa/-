from itertools import chain, combinations
from typing import Set, Dict, Any

def generate_bpa(universe: Set) -> Dict:
    """
    生成一个基于给定论域的基本概率指派 (BPA)。

    Args:
        universe: 论域，一个包含所有可能性的集合。

    Returns:
        一个字典，表示 BPA。键是论域的子集（作为 frozenset），值是对应的基本概率。
    """

    power_set = get_power_set(universe)
    bpa = {}

    # 默认的简单 BPA 生成策略：为每个非空子集分配一个相等的概率
    num_non_empty_subsets = len(power_set) - 1
    if num_non_empty_subsets > 0:
        default_probability = 1.0 / num_non_empty_subsets
        for subset in power_set:
            if subset:  # 排除空集
                bpa[_freeze_set(subset)] = default_probability
    else:
        # 如果论域为空，则 BPA 也为空（技术上讲，这种情况不常见）
        pass

    return bpa

def get_power_set(elements: Set) -> Set:
    """
    获取给定集合的幂集。

    Args:
        elements: 要获取幂集的集合。

    Returns:
        包含给定集合所有子集的集合。每个子集都是一个 frozenset，以便可以用作字典的键。
    """
    power_set = set()
    list_elements = list(elements)
    for i in range(len(elements) + 1):
        for subset in combinations(list_elements, i):
            power_set.add(frozenset(subset))
    return power_set

def _freeze_set(input_set: Set) -> frozenset:
    """
    将一个可变集合转换为不可变的 frozenset。
    """
    return frozenset(input_set)

# 示例用法
if __name__ == "__main__":
    universe = {"A", "B", "C", "D"}
    bpa = generate_bpa(universe)
    print("生成的 BPA:")
    for subset, probability in bpa.items():
        print(f"m({set(subset)}) = {probability:.3f}")

    # 验证概率和是否为 1
    sum_probabilities = sum(bpa.values())
    print(f"\n所有基本概率之和: {sum_probabilities:.3f}")
