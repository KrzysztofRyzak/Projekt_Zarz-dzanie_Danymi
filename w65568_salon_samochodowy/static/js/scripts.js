// Funkcja do potwierdzenia usunięcia samochodu
function deleteCar(carId) {
    if (confirm("Czy na pewno chcesz usunąć ten samochód?")) {
        window.location.href = `/delete/${carId}`;
    }
}
