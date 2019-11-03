$(function(){

    $('.like-btn').on('click', function(){
      likePost(this);
    });

    function likePost(thumb){

      {% if user.is_authenticated %}
        // Visual like button highlighting
        $(thumb).toggleClass('btn-like-post')

        // route: /like/(id)
        // Take the index of the current like-button and add
        // 1 to it (so it starts at 1) to match the primary-key
        // of the database

        id = $('.like-btn').index(thumb)+1
        var url = '/like/' + id.toString()
        $.ajax({
          url: url,
          data: { csrfmiddlewaretoken: '{{ csrf_token }}' },
          method: 'POST',
          success: function(){
          }
        })
      {% else %}
        window.location='/login'
      {% endif %}
    }

  });