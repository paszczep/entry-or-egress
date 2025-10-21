  const cancel = document.getElementById('try-again');

  cancel.focus();

  const TARGET = "/";
  let n = 3;
  const el = document.getElementById("sec");
  const timer = setInterval(() => {
    n--;
    if (n <= 0) {
      clearInterval(timer);
      location.replace(TARGET);
    } else {
      el.textContent = n;
    }
  }, 1000);
  