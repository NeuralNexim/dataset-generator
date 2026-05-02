from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.generator import generate_one_sample


def run_domain_selftest():
    results = {}
    for domain in DOMAIN_REGISTRY.keys():
        try:
            _ = generate_one_sample(domain)
            results[domain] = "OK"
        except Exception as e:
            results[domain] = f"FAIL: {e}"
    return results


if __name__ == "__main__":
    for d, status in run_domain_selftest().items():
        print(f"{d}: {status}")
