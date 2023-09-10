async function exchange () {
	var value = document.querySelector(".value").value;
	var select = [document.querySelector(".from").value, document.querySelector(".to").value];
	var result = await eel.exchange_rate(select[0], select[1], value)();
	document.querySelector(".result").value = result;
}