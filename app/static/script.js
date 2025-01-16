async function fetchData(endpoint,data) {
    const response = await fetch(endpoint,{
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result =await response.json();
    return result.response;
}
// Search by CVE name
document.getElementById('chat-btn').addEventListener('click', async (event) => {
    const cveName=document.getElementById('cveName').value.trim();
    if(!cveName){
        alert('Please enter a valid cve name.');
        return;
    }
    const response = await fetchData('/api/chat', { message: cveName });
    displayResponse(response);
});
// Search by Keyword
document.getElementById('search-btn').addEventListener('click', async (event) => {
   const keyword = document.getElementById('keyword').value.trim();
    if (!keyword) {
        alert('Please enter a keyword.');
        return;
    }
    const response = await fetchData('/api/search', { keyword });
    displayResponse(response);
});

// Filter by Severity
document.getElementById('filter-btn').addEventListener('click', async () => {
    const severity = document.getElementById('severity').value.trim();
    if (!severity) {
        alert('Please enter a severity level.');
        return;
    }
    const response = await fetchData('/api/filter', { severity });
    displayResponse(response);
});

//display response in the UI
function displayResponse(response) {
    const responseDiv=document.getElementById('response');
    responseDiv.style.display = 'block';
    responseDiv.textContent = response;
}