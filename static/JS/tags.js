document.addEventListener('DOMContentLoaded', () => {
    const tags = document.getElementsByClassName('tags');
    Array.from(tags).forEach(tag => {
        if (tag.innerText.trim() === 'Pendente') {
            tag.classList.add('text-white', 'bg-red', 'rounded-md', 'p-1');
        }
    });
});