#[macro_use]
extern crate quartic_equation;
use quartic_equation::qe_struct::*;
use SquareRootResult::*;

#[test]
/// Проверка биквадратного уравнения без корней
fn zero_roots() {
    let mut eq = qe_new!(1, 1, 1);
    eq.update_coefs();
    eq.calculate_roots();
    match eq.res {
        Ok(res) => match res {
            NoRoots => (),
            _ => assert!(false, "Корней не должно было быть!"),
        }
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}

#[test]
/// Проверка биквадратного уравнения с одним корнем
fn one_root() {
    const EXPECTED: f64 = 0.0;
    let mut eq = qe_new!(1, 0, 0);
    eq.update_coefs();
    eq.calculate_roots();
    match eq.res {
        Ok(res) => match res {
            OneRoot(root) => assert!(root == EXPECTED, "Корень не верный: {} != {}", root, EXPECTED),
            _ => assert!(false, "Корень должен был быть один!"),
        }
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}

#[test]
/// Проверка биквадратного уравнения с двумя корнями
fn two_roots() {
    const EXPECTED_1: f64 = -1.0;
    const EXPECTED_2: f64 = 1.0;
    let mut eq = qe_new!(1, -2, 1);
    eq.update_coefs();
    eq.calculate_roots();
    match eq.res {
        Ok(res) => match res {
            TwoRoots { root1, root2 } => {
                assert!(root1 == EXPECTED_1, "Первый корень не верный: {} != {}", root1, EXPECTED_1);
                assert!(root2 == EXPECTED_2, "Второй корень не верный: {} != {}", root2, EXPECTED_2);
            },
            _ => assert!(false, "Корня должно было быть два!"),
        }
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}

#[test]
/// Проверка биквадратного уравнения с тремя корнями
fn three_roots() {
    const EXPECTED_1: f64 = -1.0;
    const EXPECTED_2: f64 = 1.0;
    const EXPECTED_3: f64 = 0.0;
    let mut eq = qe_new!(2, -2, 0);
    eq.update_coefs();
    eq.calculate_roots();
    match eq.res {
        Ok(res) => match res {
            ThreeRoots { root1, root2, root3 } => {
                assert!(root1 == EXPECTED_1, "Первый корень не верный: {} != {}", root1, EXPECTED_1);
                assert!(root2 == EXPECTED_2, "Второй корень не верный: {} != {}", root2, EXPECTED_2);
                assert!(root3 == EXPECTED_3, "Третий корень не верный: {} != {}", root3, EXPECTED_3);
            },
            _ => assert!(false, "Корня должно было быть три!"),
        }
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}

#[test]
/// Проверка биквадратного уравнения с четырьмя корнями
fn four_roots() {
    const EXPECTED_1: f64 = -1.0;
    const EXPECTED_2: f64 = 1.0;
    const EXPECTED_3: f64 = -0.5;
    const EXPECTED_4: f64 = 0.5;
    let mut eq = qe_new!(4, -5, 1);
    eq.update_coefs();
    eq.calculate_roots();
    match eq.res {
        Ok(res) => match res {
            FourRoots { root1, root2, root3, root4 } => {
                assert!(root1 == EXPECTED_1, "Первый корень не верный: {} != {}"   , root1, EXPECTED_1);
                assert!(root2 == EXPECTED_2, "Второй корень не верный: {} != {}"   , root2, EXPECTED_2);
                assert!(root3 == EXPECTED_3, "Третий корень не верный: {} != {}"   , root3, EXPECTED_3);
                assert!(root4 == EXPECTED_4, "Четвёртый корень не верный: {} != {}", root4, EXPECTED_4);
            },
            _ => assert!(false, "Корня должно было быть четыре!"),
        }
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}
