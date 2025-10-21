(() => {
  const SECONDS = 6;

  const form = document.getElementById('confirm-form');
  const btn = document.getElementById('confirm-btn');
  const cancel = document.getElementById('cancel-link');


  cancel.focus();

  let remaining = SECONDS;
  let timer = setInterval(() => {
    remaining -= 1;
    if (remaining <= 0) {
      clearInterval(timer);
      btn.disabled = true;
      btn.textContent = 'Tak…';
      form.submit();
    } else {
      btn.textContent = `Tak (${remaining})`;
    }
  }, 1000);


  cancel.addEventListener('click', () => {
    clearInterval(timer);
    btn.textContent = 'Tak';
  });


  form.addEventListener('submit', () => clearInterval(timer));


  cancel.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') cancel.click();
  });
})();
