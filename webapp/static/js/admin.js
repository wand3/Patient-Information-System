// displayArea = user_deleted
// displayUser = deleteRole


const deleteRole = (userData) => {
  const  user_deleted = document.getElementById('deleteRole');

  user_deleted.innerHTML = '';

  //   create Element to display user role deleted   
  const userIdElement = document.createElement('p');
  userIdElement.textContent = `User ID: ${userData.id}`;


  // Append element to display area
  user_deleted.appendChild(userIdElement);
};


const getUserById = async (userId) => {
  const url = `/delete_role/${id}` // url_for()

  try {
    const response = await fetch(url, {
      method: "DELETE",
    });
    const data = await response.json();

    if (response.ok) {
      console.log(`User ${id} role deleted`)
      } else {
      console.log(`Failed to delete User ${id} role`)};
    } catch (error) {
    console.log('Error:', error)
  }
};


// handle button click 
const handleButtonClick = () => {
    const id = getUserById(id);
};

// attach click event listener to your button 
const button = document.getElementById('button');
button.addEventListener('click', handleButtonClick);
