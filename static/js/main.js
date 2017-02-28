/*
 * @Author: Sidharth Mishra
 * @Date:   2017-02-27 14:24:33
 * @Last Modified by:   Sidharth Mishra
 * @Last Modified time: 2017-02-27 21:13:40
 */

'use strict';

var user_name = user ? 'manager@amc.com' : 'employee@amc.com'



function reset_task_creation_form() {

    jQuery('#task_name').val('')
    jQuery('#recipient_email_address').val('')
    jQuery('#task_description').val('')
}



function create_task(event) {

    event.preventDefault()

    let task_name = jQuery('#task_name').val()
    let recipient_email_address = jQuery('#recipient_email_address').val()
    let task_description = jQuery('#task_description').val()

    if (task_name === "" || recipient_email_address === "" || task_description === "") {

        alert('Please complete all the fields')
        return
    }

    jQuery.ajax({
        url: "/create_task",
        type: "POST",
        data: {
            "task_name": task_name,
            "recipient_email_address": recipient_email_address,
            "task_description": task_description,
            "setter_email_address": "manager@amc.com"
        },
        success: function() {

            reset_task_creation_form()
            get_all_created_tasks()
        },
        error: function(error, xhr, status) {

            alert('oops! ' + status)
            alert(JSON.stringify(error))
        }
    })
}


// for now, using hard-coded email for task_owner
// "employee@amc.com"
function get_all_tasks_assigned() {

    jQuery.ajax({
        url: "/get_all_tasks_assigned",
        type: "POST",
        data: {
            task_owner: user_name
        },
        dataType: "JSON",
        success: function(data) {

            render_assigned_task_list(data)
        },
        error: function(error, xhr, status) {

            console.log(JSON.stringify(error))
        }
    })
}


function render_assigned_task_list(json_data) {

    // sample formats of output and input
    //
    // <li class="wf-selected">
    //     <div class="w-form">
    //         <div id="task_listing_li" class="w-clearfix taskcreatedli">
    //             <label class="tasknameli" for="name-2">Task Name</label>
    //             <label class="taskcreationdateli">TaskCreationDate</label>
    //             <label class="taskcompletiondateli">taskCompletionDate</label>
    //             <label class="taskassignedtoli">Assigned To</label>
    //             <label class="taskdescriptionli" for="email">Task Description</label>
    //             <div class="w-checkbox taskcompletionbox">
    //                 <input class="w-checkbox-input" id="mark_as_complete" name="mark_as_complete" type="checkbox">
    //                 <label class="w-form-label" for="checkbox">Mark As Completed</label>
    //             </div>
    //         </div>
    //     </div>
    // </li>
    // "{ "taskId": "7838322c-ddd7-45c9-af72-05da684c9871",
    //  "task_name": "clean 1",
    //  "description": "clean",
    //  "setup_date": "2017-02-27 18:33:33.785809",
    //  "completion_date": "None",
    //  "is_complete": false,
    //  "task_setter": "manager@amc.com",
    //  "assigned_to": "employee@amc.com"}"

    // clear the ul
    jQuery('#myTaskList').html()

    // rebuild the ul
    jQuery.each(json_data, function(index, value) {

        let li_str = '<li class="wf-selected">' +
            '<div class="w-form">' +
            '<div id="task_listing_li_' + JSON.parse(value)['taskId'] + '" class="w-clearfix taskcreatedli">' +
            '<label class="tasknameli">' + 'Task Name:&nbsp;&nbsp;' + JSON.parse(value)['task_name'] + '</label>' +
            '<label class="taskcreationdateli">' + 'Task Creation Date:&nbsp;&nbsp;' + JSON.parse(value)['setup_date'] + '</label>' +
            '<label class="taskcompletiondateli">' + 'Task Completion Date:&nbsp;&nbsp;' + (JSON.parse(value)['completion_date'] === 'None' ? 'WIP' : JSON.parse(value)['completion_date']) + '</label>' +
            '<label class="taskassignedtoli">' + 'Assigned To:&nbsp;&nbsp;' + JSON.parse(value)['assigned_to'] + '</label>' +
            '<label class="taskdescriptionli">' + 'Task Description:&nbsp;&nbsp;' + JSON.parse(value)['description'] + '</label>' +
            '<div class="w-checkbox taskcompletionbox">' +
            (JSON.parse(value)['is_complete'] ? ('<label class="w-form-label">' + 'Task Status:&nbsp;&nbsp;' + 'COMPLETE' + '</label>') :
                ('<input class="w-checkbox-input completion_checkbox" id="mark_as_complete_' + JSON.parse(value)['taskId'] + '" name="mark_as_complete" type="checkbox">' +
                    '<label class="w-form-label">' + 'Mark as complete' + '</label>')) +
            '</div>' +
            '</div>' +
            '</div>' +
            '</li>'

        jQuery('#myTaskList').append(li_str)
    })

    jQuery('.completion_checkbox').unbind('change').bind('change', function(event) {

        update_task_status(event)
    })
}



function get_all_created_tasks() {

    jQuery.ajax({
        url: "/get_all_created_tasks",
        type: "POST",
        data: {
            task_owner: user_name
        },
        dataType: "JSON",
        success: function(data) {

            render_created_task_list(data)
        },
        error: function(error, xhr, status) {

            console.log(JSON.stringify(error))
        }
    })
}


function render_created_task_list(json_data) {

    // sample formats of output and input
    //
    // <li class="wf-selected">
    //     <div class="w-form">
    //         <div id="task_listing_li" class="w-clearfix taskcreatedli">
    //             <label class="tasknameli" for="name-2">Task Name</label>
    //             <label class="taskcreationdateli">TaskCreationDate</label>
    //             <label class="taskcompletiondateli">taskCompletionDate</label>
    //             <label class="taskassignedtoli">Assigned To</label>
    //             <label class="taskdescriptionli" for="email">Task Description</label>
    //             <div class="w-checkbox taskcompletionbox">
    //                 <input class="w-checkbox-input" id="mark_as_complete" name="mark_as_complete" type="checkbox">
    //                 <label class="w-form-label" for="checkbox">Mark As Completed</label>
    //             </div>
    //         </div>
    //     </div>
    // </li>
    // "{ "taskId": "7838322c-ddd7-45c9-af72-05da684c9871",
    //  "task_name": "clean 1",
    //  "description": "clean",
    //  "setup_date": "2017-02-27 18:33:33.785809",
    //  "completion_date": "None",
    //  "is_complete": "False",
    //  "task_setter": "manager@amc.com",
    //  "assigned_to": "employee@amc.com"}"

    // clear the ul
    jQuery('#tasksAssigned').html('')

    // re-build the ul
    jQuery.each(json_data, function(index, value) {

        let li_str = '<li class="wf-selected">' +
            '<div class="w-form">' +
            '<div id="task_listing_li_' + JSON.parse(value)['taskId'] + '" class="w-clearfix taskcreatedli">' +
            '<label class="tasknameli">' + 'Task Name:&nbsp;&nbsp;' + JSON.parse(value)['task_name'] + '</label>' +
            '<label class="taskcreationdateli">' + 'Task Creation Date:&nbsp;&nbsp;' + JSON.parse(value)['setup_date'] + '</label>' +
            '<label class="taskcompletiondateli">' + 'Task Completion Date:&nbsp;&nbsp;' + (JSON.parse(value)['completion_date'] === 'None' ? 'WIP' : JSON.parse(value)['completion_date']) + '</label>' +
            '<label class="taskassignedtoli">' + 'Assigned To:&nbsp;&nbsp;' + JSON.parse(value)['assigned_to'] + '</label>' +
            '<label class="taskdescriptionli">' + 'Task Description:&nbsp;&nbsp;' + JSON.parse(value)['description'] + '</label>' +
            '<div class="w-checkbox taskcompletionbox">' +
            '<label class="w-form-label">' + 'Task Status:&nbsp;&nbsp;' + (JSON.parse(value)['is_complete'] == false ? 'WIP' : 'COMPLETE') + '</label>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</li>'


        jQuery('#tasksAssigned').append(li_str)
    })
}


// update the task status on the checking the completion checkbox
function update_task_status(event) {

    let id = jQuery(event.target).attr('id')
    let uuid = id.split('mark_as_complete_')[1]

    jQuery.ajax({
        url: '/mark_task_complete',
        type: 'POST',
        data: {
            'task_id': uuid
        },
        success: function(data) {

            console.debug()
            
            let parent_div = jQuery(event.target).parent()
            jQuery(parent_div).html('<label class="w-form-label">' + 'Task Status:&nbsp;&nbsp;' + 'COMPLETE' + '</label>')
            let grand_parent = jQuery(parent_div).parent()
            let completion_date_child = jQuery(grand_parent).children('.taskcompletiondateli')
            jQuery(completion_date_child).html('<label class="taskcompletiondateli">' + 'Task Completion Date:&nbsp;&nbsp;' + (JSON.parse(data)['completion_date'] === 'None' ? 'WIP' : JSON.parse(data)['completion_date']) + '</label>')
        },
        error: function(error, xhr, status) {

            console.log(JSON.stringify(error))
        }
    })
}



jQuery('document').ready(function() {

    jQuery('.amcbutton').unbind('click').bind('click', function(event) {

        create_task(event)
    })

    if (jQuery('#tasksAssigned')) {

        get_all_created_tasks()
    }

    get_all_tasks_assigned()
})
