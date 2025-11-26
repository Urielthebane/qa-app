async function ask() {
    const q = document.getElementById("question").value.trim();
    if (!q) return alert("Type something!");
    
    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("answer").innerHTML = "";

    const res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: q})
    });
    const data = await res.json();
    
    document.getElementById("loading").classList.add("hidden");
    document.getElementById("answer").innerHTML = data.answer || data.error;
}