use std::process::{Command, Stdio};

#[test]
/// Проверка ввода трёх коэффициентов (происходит расчёт ответа)
fn three_coefs_input() {
    const EXPECTED: &str = "Корней нет\n";
    match Command::new("cargo").arg("build").stdout(Stdio::null()).spawn() {
        Ok(..) => {
            let output = Command::new("cargo").args(["run", "1", "1", "1"]).output().expect("command cargo run failed");
            assert!(output.status.success());
            let str = String::from_utf8_lossy(&output.stdout);
            assert!(str == EXPECTED, "Неверный ответ: \"{}\" != \"{}\"", str, EXPECTED);
        },
        Err(err) => assert!(false, "Ошибка: {}", err),
    }
}
