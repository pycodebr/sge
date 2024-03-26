function DeleteConfirm(pk) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-success',
        },
        buttonsStyling: true
    })

    swalWithBootstrapButtons.fire({
        title: 'Você tem certeza?',
        text: "Você não poderá reverter isso!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: '<i class="icon-copy dw dw-delete-3"></i> Deletar',
        cancelButtonText: '<i class="icon-copy dw dw-cancel"></i> Cancelar',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            swalWithBootstrapButtons.fire(
                'Deletado!',
                'REGISTRO DELETADO COM SUCESSO!',
                'success'
            )
            var url = '../' + parseInt(pk) + '/delete/';

            setTimeout(function () {
                location.href = url;
            }, 800);
        } else if (
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado!',
                'O REGISTRO <b>NÃO</b> FOI DELETADO!',
                'info'
            )
        }
    });
}