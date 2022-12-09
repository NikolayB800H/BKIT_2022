#[macro_use]
extern crate quartic_equation;
use quartic_equation::qe_struct::*;
use SquareRootResult::*;

#[test]
fn one_root() {
    const EXPECTED: f64 = 1.0;
    let mut eq = qe_new!(1, -2, 1);
    eq.get_coefs();
    eq.calculate_roots();
    match eq.res {
        OneRoot(root) => assert!(root == EXPECTED, "Корень не верный: {} != {}", root, EXPECTED),
        _ => assert!(false, "Корень должен был быть один!"),
    }
    assert!(true);
}

#[test]
fn two_roots() {
    const EXPECTED_1: f64 = 1.0;
    const EXPECTED_2: f64 = 2.0;
    let mut eq = qe_new!(1, -3, 2);
    eq.get_coefs();
    eq.calculate_roots();
    match eq.res {
        TwoRoots { root1, root2 } => {
            assert!(root1 == EXPECTED_1, "Первый корень не верный: {} != {}", root1, EXPECTED_1);
            assert!(root2 == EXPECTED_2, "Второй корень не верный: {} != {}", root2, EXPECTED_2);
        },
        _ => assert!(false, "Корня должно было быть два!"),
    }
    assert!(true);
}
