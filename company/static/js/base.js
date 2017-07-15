// Для модального окна 'ЗАКАЗАТЬ ЗВОНОК'
// После клика по input окну если есть текст, он исчезает, 

$( 'input#id_name' ).on( 'select click', function( evt ) {
  if ($(evt.target).val()!==0){
    $(evt.target).val('');
	}
  })

$( 'input#id_phone_number' ).on( 'select click', function( evt ) {
  if ($(evt.target).val()!==0){
    $(evt.target).val('');
	}
  })

$( 'textarea#id_question' ).on( 'select click', function( evt ) {
  if ($(evt.target).val()!==0){
    $(evt.target).val('');
	}
  })
