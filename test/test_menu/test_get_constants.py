from click.testing import CliRunner
import test.test_helper_functions as helper_functions
from src.calculator import calculator


# Test Addition
def test_getting_constants():
    runner = CliRunner()
    helper_functions._clear_calculator(runner)
    result = runner.invoke(calculator.menu, ['--get-constants'])
    assert result.exit_code == 0
    assert result.output == "pi = 3.14159265358979323846\n" \
                            "squareroot_2 = 1.41421356237309504880\n" \
                            "squareroot_3 = 1.73205080756887729352\n" \
                            "golden_ratio = 1.61803398874989484820\n" \
                            "euler = 2.71828182845904523536\n" \
                            "euler_mascheroni = 0.57721566490153286060\n" \
                            "apery = 1.20205690315959428539\n" \
                            "erdos_borwein = 1.60669515241529176378\n" \
                            "ramanujan_soldner = 1.45136923488338105028\n" \
                            "lemniskat = 2.62205755429211981046\n" \
                            "legendre = 1.08366\n" \
                            "laplace_limit = 0.66274341934918158097\n" \
                            "catalan = 0.91596559417721901505\n" \
                            "meissel_mertens = 0.26149721284764278375\n" \
                            "glaisher_kinkelin = 1.28242712910062263687\n" \
                            "cahen = 1.73205080756887729352\n" \
                            "sierpinski = 2.58498175957925321706\n" \
                            "landau_ramanujan = 0.76422365358922066299\n" \
                            "gieseking = 1.01494160640965362502\n" \
                            "bernstein = 0.28016949902386913303\n" \
                            "brun = 1.90216058\n" \
                            "twin_prime = 0.66016181584686957392\n" \
                            "golomb_dickman = 0.62432998854355087099\n" \
                            "chintschin = 2.68545200106530644530\n" \
                            "chintschin_levy = 1.18656911041562545282\n" \
                            "mills = 1.30637788386308069046\n" \
                            "liebs = 1.53960071783900203869\n" \
                            "niven = 1.70521114010536776428\n" \
                            "gaus_kusmin_wirsing = 0.30366300289873265859\n" \
                            "porter = 1.46707807943397547289\n" \
                            "chaitin = 0.0078749969978123844\n" \
                            "alladi_grinstead = 0.80939402054063913071\n" \
                            "feigenbaum_1 = 4.66920160910299067185\n" \
                            "feigenbaum_2 = 2.50290787509589282228\n" \
                            "fransen_robinson = 2.80777024202851936522\n" \
                            "lengyel = 1.09868580552518701\n" \
                            "hafner_sarnak_mccurley = 0.35323637185499598454\n" \
                            "backhouse = 1.45607494858268967139\n" \
                            "viswanath = 1.1319882487943\n" \
                            "embree_trefethen = 0.70258\n\n"