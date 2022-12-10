extern crate quartic_equation;
use quartic_equation::qe_struct::*;
use SquareRootResult::*;
use std::env;

fn main() {
    let mut v: Vec::<String> = env::args().collect();
    v.remove(0);
    let mut eq = Equation::new(v);
    eq.update_coefs();
    eq.calculate_roots();
    let res_str = match eq.res {
        Ok(res) => match res {
            NoRoots => format!("Корней нет"),
            OneRoot(rt) => format!("Один корень: {}.", rt),
            TwoRoots {
                root1,
                root2
            } => format!("Два корня: {} и {}.", root1, root2),
            ThreeRoots {
                root1,
                root2,
                root3
            } => format!("Три корня: {}; {} и {}.", root1, root2, root3),
            FourRoots {
                root1,
                root2,
                root3,
                root4
            } => format!("Четыре корня: {}; {}; {} и {}.", root1, root2, root3, root4),
        },
        Err(err) => format!("Ошибка: {}.", err),
    };
    println!("{}", res_str);
}
