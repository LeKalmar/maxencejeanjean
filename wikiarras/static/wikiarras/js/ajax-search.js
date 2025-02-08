// AJAX pour afficher les résultats pendant la saisie
document.getElementById('search-input').addEventListener('input', function() {
    var query = this.value;
    
    if (query.length > 2) {  // On commence à chercher après 3 caractères
        fetch(`/wiki/search/ajax/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                let resultsHtml = '<ul>';
                data.results.forEach(page => {
                    resultsHtml += `<li><a href="/wiki/page/${page.id}/">${page.title}</a></li>`;
                });
                resultsHtml += '</ul>';
                document.getElementById('search-results').innerHTML = resultsHtml;
            });
    } else {
        document.getElementById('search-results').innerHTML = '';  // Masquer les résultats si moins de 3 caractères
    }
});