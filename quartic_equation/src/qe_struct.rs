use std::io;

#[derive(Debug, Copy, Clone)]
///Тип решения квадратного уравнения
pub enum SquareRootResult {
    /// Unit-тип
    NoRoots,
    /// Один корень - кортежная структура
    OneRoot(f64),
    /// С-подобная структура
    TwoRoots { root1: f64, root2: f64 },
}

#[derive(Debug, Clone)]
/// Структура, соответствующая уравнению
pub struct Equation {
    /// Коэффициент A
    pub c_a: f64,
    /// Коэффициент B
    pub c_b: f64,
    /// Коэффициент C
    pub c_c: f64,
    /// Дискриминант
    pub diskr: f64,
    /// Корни
    pub res: SquareRootResult,
    /// Коэффициенты на вход new
    pub coefs: Vec<String>,
}

#[macro_export]
/// При получении коэффициента был повторяющийся код
macro_rules! my_macro {
    ( $x:expr , $y:tt ) => {
        match $x.trim().parse() {
            Ok(val) => {
                $y val;
            }
            Err(_) => ()
        }
    };
}

#[macro_export]
/// Более удобный Equation new
macro_rules! qe_new {
    ( $a:expr , $b:expr , $c:expr ) => {
        Equation::new(vec![$a.to_string(), $b.to_string(), $c.to_string()]);
    };
}

impl Equation {
    /// Функция создания
    pub fn new(coefs: Vec::<String>) -> Self {
        Self {
            c_a: 0.0,
            c_b: 0.0,
            c_c: 0.0,
            diskr: 0.0,
            res: SquareRootResult::NoRoots,
            coefs,
        }
    }

    /// Функция вычисления корней
    pub fn calculate_roots(&mut self) {
        self.diskr = self.c_b.powi(2) - 4.0 * self.c_a * self.c_c;
        self.res = {
            if self.diskr < 0.0 {
                SquareRootResult::NoRoots
            } else if self.diskr == 0.0 {
                let rt = -self.c_b / (2.0 * self.c_a);
                SquareRootResult::OneRoot(rt)
            } else {
                let rt1 = (-self.c_b - self.diskr.sqrt()) / (2.0 * self.c_a);
                let rt2 = (-self.c_b + self.diskr.sqrt()) / (2.0 * self.c_a);
                SquareRootResult::TwoRoots {
                    root1: rt1,
                    root2: rt2,
                }
            }
        };
    }

    /// Ввод одного коэффициента
    fn get_coef(&mut self, index: i8, message: &str) -> f64 {
        let mut input = String::new();
        if self.coefs.len() > index as usize{
            input = self.coefs[index as usize].clone();
            my_macro!(input, return)
        }
        return loop {
            input.clear();
            println!("{}", message);
            io::stdin()
                .read_line(&mut input)
                .expect("Неверно введена строка");
            my_macro!(input, break)
        };
    }

    /// Обновление коэффициентов уравнения
    pub fn get_coefs(&mut self) -> () {
        self.c_a = self.get_coef(0, "Введите коэффициент A: ");
        self.c_b = self.get_coef(1, "Введите коэффициент B: ");
        self.c_c = self.get_coef(2, "Введите коэффициент C: ");
    }
}
