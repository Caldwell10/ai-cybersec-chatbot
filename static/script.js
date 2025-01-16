async function fetchData(endpoint, data) {
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
    const result = await response.json();
    return result.response;
}

// Search by CVE name
document.getElementById('chat-btn').addEventListener('click', async () => {
    const cveName = document.getElementById('cveName').value.trim();
    if (!cveName) {
        alert('Please enter a CVE name.');
        return;
    }
    const response = await fetchData('/api/chat', { message: cveName });
    displayResponse(response);
});

// Search by Keyword
document.getElementById('search-btn').addEventListener('click', async () => {
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

// Display response in the UI
function displayResponse(response) {
    const responseDiv = document.getElementById('response');
    responseDiv.style.display = 'block';

    // Clear previous responses
    responseDiv.innerHTML = '';

    // Check if response is a single string
    if (typeof response === 'string') {
        responseDiv.textContent = response;
        return;
    }

    // Format response as cards (assuming response is an array)
    response.forEach(item => {
        const card = document.createElement('div');
        card.className = 'response-card';
        card.innerHTML = `
            <h4>${item.name || 'CVE Name'}</h4>
            <p><strong>Description:</strong> ${item.description || 'N/A'}</p>
            <p><strong>Severity:</strong> ${item.severity || 'N/A'}</p>
            <p><strong>Published Date:</strong> ${item.date || 'N/A'}</p>
        `;
        responseDiv.appendChild(card);
    });
}


// Show the loading spinner
function showSpinner() {
    document.getElementById('loading-spinner').style.display = 'block';
}

// Hide the loading spinner
function hideSpinner() {
    document.getElementById('loading-spinner').style.display = 'none';
}

// Update fetchData function to show spinner while fetching data
async function fetchData(endpoint, data) {
    showSpinner(); // Show spinner
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.status}`);
        }

        const result = await response.json();
        return result.response;
    } catch (error) {
        console.error('Error fetching data:', error);
        return `An error occurred: ${error.message}`;
    } finally {
        hideSpinner(); // Hide spinner
    }
}


