// displayArea = user_deleted
// displayUser = deleteRole


const deleteRole = (userDate) => {
  const  user_deleted = document.getElementById('deleteRole');

  user_deleted.innerHTML = '';

  //   create Element to display user role deleted   
  const userIdElement = document.createElement('p');
  userIdElement.textContent = `User ID: ${userData.id}`;


  // Append element to display area
  user_deleted.appendChild(userIdElement);
};


const getUserById = async (userId) => {
  const url = `http://`
}

