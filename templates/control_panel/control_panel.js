const dirTreeEl = document.getElementById('dirTree');
const fileListEl = document.getElementById('file-list');

// Başlangıç dizini (backend ile değiştirilebilir)
const rootPath = "C:/Users/ubuntu/Desktop";

// API çağrısı yapıp dizin içeriğini alır
async function fetchDirContent(path) {
  try {
    const res = await fetch(`http://localhost:5000/api/list_dir?path=${encodeURIComponent(path)}`);
    if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
    return await res.json();
  } catch (err) {
    alert("Failed to load directory content: " + err.message);
    return null;
  }
}

// Ağaçta bir klasör düğümü oluşturur
function createFolderNode(name, fullPath) {
  const li = document.createElement('li');
  li.classList.add('folder');
  li.dataset.path = fullPath;

  const span = document.createElement('span');
  span.textContent = name;
  li.appendChild(span);

  const childrenUl = document.createElement('ul');
  childrenUl.style.display = 'none';
  li.appendChild(childrenUl);

  // Klasör tıklanınca aç/kapa
  span.addEventListener('click', async () => {
    if (li.classList.contains('expanded')) {
      // Kapat
      li.classList.remove('expanded');
      childrenUl.style.display = 'none';
    } else {
      // Aç
      li.classList.add('expanded');
      childrenUl.style.display = 'block';
      if (childrenUl.childElementCount === 0) {
        // İçeriği getir ve ekle
        const data = await fetchDirContent(fullPath);
        if (data) {
          for (const folder of data.directories) {
            const childFolder = createFolderNode(folder, fullPath + '/' + folder);
            childrenUl.appendChild(childFolder);
          }
          for (const file of data.files) {
            const fileLi = document.createElement('li');
            fileLi.classList.add('file');
            fileLi.textContent = file;
            fileLi.dataset.path = fullPath + '/' + file;
            fileLi.addEventListener('click', () => {
              alert('File selected: ' + fileLi.dataset.path);
              // Burada dosya ile yapılacak başka işlemler eklenebilir
            });
            childrenUl.appendChild(fileLi);
          }
        }
      }
    }
    // Sağ tarafta seçilen klasör içeriğini göster
    showFolderContent(fullPath);
  });

  return li;
}

// Sağdaki alanda klasör içeriğini gösterir (liste olarak)
async function showFolderContent(path) {
  const data = await fetchDirContent(path);
  if (!data) {
    fileListEl.textContent = 'Failed to load folder content.';
    return;
  }
  let output = `Directories:\n${data.directories.join('\n') || '(none)'}\n\nFiles:\n${data.files.join('\n') || '(none)'}`;
  fileListEl.textContent = output;
}

// İlk olarak root dizini göster
async function init() {
  const rootNode = createFolderNode(rootPath, rootPath);
  dirTreeEl.appendChild(rootNode);
}

init();

