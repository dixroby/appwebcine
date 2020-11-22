function confirmarEliminacion (id,peli){
 
    Swal.fire({
        title: 'Deseas eliminar la pelicula , '+peli+'?',
        text: "No podrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si eliminar'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir
          window.location.href = "/eliminar-pelicula/"+id + "/";
        }
      })
}