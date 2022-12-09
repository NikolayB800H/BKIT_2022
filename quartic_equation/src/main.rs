extern crate quartic_equation;
use quartic_equation::qe_struct::*;
use SquareRootResult::*;
use std::env;

fn main() {
    let mut v: Vec::<String> = env::args().collect();
    v.remove(0);
    let mut eq = Equation::new(v);
    eq.get_coefs();
    eq.calculate_roots();
    let text_res = match eq.res {
        NoRoots => format!("Корней нет"),
        OneRoot(rt) => format!("Один корень => {}", rt),
        TwoRoots { root1, root2 } => format!("Два корня => {} и {}", root1, root2),
    };
    println!("{}", text_res);
}
