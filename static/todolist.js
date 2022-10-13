$(document).ready(() => {
    $.get('/todolist/json', (tasks) => {
      $('#tasks-section').append(`
        <h1 id="num-of-tasks">
          ${tasks.length} tasks
        </h1>
      `)
      tasks.forEach((task) => {
        $('#tasks-section').append(`
          <div id="task-${task.id}" data-aos="flip-up">
            <div>
              <div>
                <h2>
                  ${task.fields.title}
                </h2>
                <p>
                  ${task.fields.date}
                </p>
                <p>
                  ${task.fields.description}
                </p>
              </div>
            </div>
            <button id="delete-${task.id}">
              Delete
            </button>
          </div>
        `)
        $(`#delete-${task.id}`).click(() => {
          console.log("DELETE")
          $.ajax({
            url: `/todolist/delete/${task.id}`,
            type: 'GET',
            credentials: 'include',
            success: () => $(`#task-${task.id}`).remove()
          })
        })
      })
    })
    
  
    $('#creating-new-task-form').submit((e) => {
      e.preventDefault()
      $.ajax({
        url: '/todolist/add/',
        type: 'POST',
        credentials: 'include',
        dataType: 'json',
        data: $('#creating-new-task-form').serialize(),
        success: (resp) => {
          $('#tasks').append(`
            <div id="task-${resp.id}" data-aos="flip-up">
              <div>
                <div>
                  <h2>
                    ${resp.title}
                  </h2>
                  <p>
                    ${resp.date}
                  </p>
                  <p>
                    ${resp.description}
                  </p>
                </div>
              </div>
              <button id="delete-${resp.id}">
                Delete
              </button>
            </div>
          `)
          $(`#delete-${task.id}`).click(() => {
            $.ajax({
              url: `/todolist/delete-${task.id}`,
              type: 'DELETE',
              credentials: 'include',
              dataType: 'json',
              success: () => $(`#task-${task.id}`).remove()
            })
          })
          $('#creating-new-task-modal').addClass('hidden')
        }
      })
    })

    $('#open-button').click(() => {
      $('#creating-new-task-modal').removeClass('hidden')
     
    })
    
    $('#close-button').click(() => {
      $('#creating-new-task-modal').addClass('hidden')
    })
  })