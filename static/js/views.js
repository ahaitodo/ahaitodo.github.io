/* Client-side views reader + optional increment proxy call
   - Reads `static/data/views.json` from raw.githubusercontent.com and displays counts
   - To increment, configure `site.viewsApi` in `_config.yml` to point to a secure server-side proxy
     which triggers the `increment_views` workflow using a GitHub token. */
(function () {
  function getRepoRawUrl() {
    // Hard-coded owner/repo for this site
    return 'https://raw.githubusercontent.com/ahaitodo/ahaitodo.github.io/main/static/data/views.json';
  }

  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = String(text);
  }

  function loadCounts() {
    fetch(getRepoRawUrl(), {cache: 'no-cache'})
      .then(function (r) { if (!r.ok) throw new Error('fetch failed'); return r.json(); })
      .then(function (data) {
        var path = window.location.pathname || '/';
        // Try matching exact path, then try with and without trailing slash
        var val = data[path] || data[path + (path.endsWith('/') ? 'index.html' : '')] || data[path.replace(/\/index.html$/, '')] || 0;
        setText('busuanzi_value_page_pv', val || 0);

        // compute site total
        var total = 0;
        Object.keys(data).forEach(function (k) { total += Number(data[k] || 0); });
        setText('busuanzi_value_site_pv', total);
      })
      .catch(function () {
        // keep defaults (fallback script already sets 0)
      });
  }

  // optional increment via proxy: site.viewsApi should be set as absolute URL
  function tryIncrement() {
    try {
      if (!window.blog || !window.blog.viewsApi) return;
      var api = window.blog.viewsApi;
      var path = window.location.pathname || '/';
      // send POST { page: path }
      fetch(api, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: path })
      }).catch(function () {});
    } catch (e) {}
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { loadCounts(); tryIncrement(); });
  } else {
    loadCounts(); tryIncrement();
  }
})();
