document.addEventListener("DOMContentLoaded", () => {
  // Mock data
  const users = [
    { id: 1, name: "Rawan", role: "Admin" },
    { id: 2, name: "Omar", role: "User" },
    { id: 3, name: "Sara", role: "Moderator" }
  ];

  // Render users
  function renderUsers(data) {
    const tbody = document.querySelector("#userTable tbody");
    tbody.innerHTML = "";
    data.forEach(u => {
      const row = `<tr><td>${u.id}</td><td>${u.name}</td><td>${u.role}</td></tr>`;
      tbody.innerHTML += row;
    });
  }
  renderUsers(users);

  // Sidebar navigation
  document.querySelectorAll(".sidebar a").forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      const sectionName = e.target.getAttribute("data-section");

      // Hide all sections
      document.querySelectorAll(".card").forEach(card => card.style.display = "none");

      // Show selected section
      document.getElementById(sectionName).style.display = "block";
    });
  });
});