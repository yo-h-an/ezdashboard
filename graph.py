import pandas as pd
import time
import datetime as dt

import pandas as pd

# Sample DataFrame structure
data = {
    'task_name': ['Task 1', 'Task 1', 'Task 1', 'Task 2', 'Task 2', 'Task 2', 'Task 3', 'Task 3', 'Task 3'],
    'subtask_name': ['Subtask 1.1', 'Subtask 1.2', 'Subtask 1.3', 'Subtask 2.1', 'Subtask 2.2', 'Subtask 2.3', 'Subtask 3.1', 'Subtask 3.2', 'Subtask 3.3'],
    'category': ['Design', 'Design', 'Design', 'Development', 'Development', 'Development', 'Testing', 'Testing', 'Testing'],
    'start_date': ['2023-01-01', '2023-01-01', '2023-01-03', '2023-01-08', '2023-01-08', '2023-01-11', '2023-01-16', '2023-01-16', '2023-01-20'],
    'end_date': ['2023-01-02', '2023-01-03', '2023-01-07', '2023-01-10', '2023-01-11', '2023-01-15', '2023-01-18', '2023-01-20', '2023-01-23'],
}

df = pd.DataFrame(data)

# Function to assign y-values to each task based on category and potential overlap
def assign_y_values(df):
    category_y_mapping = {}
    current_y = 0  # Initial y value

    y_values = []
    for _, row in df.iterrows():
        category = row['category']
        
        # Check if this category already has a y-value assigned
        if category not in category_y_mapping:
            category_y_mapping[category] = current_y
            current_y += 1
        
        # Assign the y value for the task in this category
        y_values.append(category_y_mapping[category])

    # Add the generated y-values to the DataFrame
    df['y_value'] = y_values
    return df

# Generate y-values and update the DataFrame
df_with_y_values = assign_y_values(df)

# Output the DataFrame with assigned y-values
print(df_with_y_values)


# Helper function to convert a date string to a Highcharts-compatible timestamp
def to_timestamp(date_str):
    date_obj = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
    return int(time.mktime(date_obj.timetuple())) * 1000  # Convert to milliseconds

# Function to create drilldown_tasks from DataFrame
def create_drilldown_tasks(df):
    # Group the DataFrame by the 'drilldown_id' column to get tasks and their subtasks
    drilldown_tasks = []
    grouped = df.groupby('drilldown_id')
    
    for drilldown_id, group in grouped:
        # Get the task name (assuming each subtask belongs to the same task)
        task_name = group['task_name'].iloc[0]
        
        # Create a list of subtasks for each group
        subtasks = []
        for _, row in group.iterrows():
            subtask = {
                'name': row['subtask_name'],
                'start': to_timestamp(row['start_date']),
                'end': to_timestamp(row['end_date']),
                'y': row['y_value']
            }
            subtasks.append(subtask)
        
        # Create the drilldown dictionary entry
        drilldown_tasks.append({
            'id': drilldown_id,
            'name': task_name + ' Subtasks',
            'data': subtasks
        })
    
    return drilldown_tasks

# Example DataFrame
data = {
    'task_name': ['Task 1', 'Task 1', 'Task 1', 'Task 2', 'Task 2', 'Task 2', 'Task 3', 'Task 3', 'Task 3'],
    'subtask_name': ['Subtask 1.1', 'Subtask 1.2', 'Subtask 1.3', 'Subtask 2.1', 'Subtask 2.2', 'Subtask 2.3', 'Subtask 3.1', 'Subtask 3.2', 'Subtask 3.3'],
    'category': ['Design', 'Design', 'Design', 'Development', 'Development', 'Development', 'Testing', 'Testing', 'Testing'],
    'start_date': ['2023-01-01', '2023-01-01', '2023-01-03', '2023-01-08', '2023-01-08', '2023-01-11', '2023-01-16', '2023-01-16', '2023-01-20'],
    'end_date': ['2023-01-02', '2023-01-03', '2023-01-07', '2023-01-10', '2023-01-11', '2023-01-15', '2023-01-18', '2023-01-20', '2023-01-23'],
    'y_value': [0, 0.1, 0, 1, 1.1, 1, 2, 2.1, 2],
    'drilldown_id': ['task1', 'task1', 'task1', 'task2', 'task2', 'task2', 'task3', 'task3', 'task3']
}

df = pd.DataFrame(data)

# Generate the drilldown_tasks dictionary from the DataFrame
drilldown_tasks = create_drilldown_tasks(df)

# Print the generated drilldown_tasks dictionary
for task in drilldown_tasks:
    print(task)


import datetime as dt
import time

# Helper function to convert datetime.date to Highcharts timestamp (milliseconds)
def to_timestamp(date_obj):
    return int(time.mktime(date_obj.timetuple())) * 1000  # Convert to milliseconds

# Wrapper function to create a Gantt chart HTML with same-chart drilldown support
def create_gantt_chart_html(file_name, tasks, drilldown_tasks):
    # Define the HTML template with Highcharts Gantt and Drilldown integration
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Drilldown Gantt Chart Example</title>
        <script src="https://code.highcharts.com/gantt/highcharts-gantt.js"></script>
        <script src="https://code.highcharts.com/modules/drilldown.js"></script>
    </head>
    <body>
        <div id="gantt-chart-container" style="width: 100%; height: 500px;"></div>

        <script>
            document.addEventListener('DOMContentLoaded', function () {{
                Highcharts.ganttChart('gantt-chart-container', {{
                    title: {{
                        text: 'Project Timeline with Drilldown - Gantt Chart'
                    }},
                    xAxis: {{
                        type: 'datetime',
                        min: {to_timestamp(dt.date(2023, 1, 1))},
                        max: {to_timestamp(dt.date(2023, 2, 1))},
                        tickInterval: 24 * 3600 * 1000 * 7  // Weekly ticks
                    }},
                    yAxis: {{
                        categories: {list(set(task['category'] for task in tasks))},
                        gridLineWidth: 1,
                        title: null
                    }},
                    series: [{{
                        name: 'Project Tasks',
                        data: {tasks},
                        colorByPoint: true,
                        dataLabels: {{
                            enabled: true,
                            format: '{{point.name}}'
                        }},
                        allowPointSelect: true,
                        borderRadius: 3  // Rounded corners for clarity
                    }}],
                    drilldown: {{
                        activeAxisLabelStyle: {{
                            color: '#666',
                            cursor: 'default'
                        }},
                        series: {drilldown_tasks}  // Drilldown data for subtasks
                    }},
                    plotOptions: {{
                        series: {{
                            events: {{
                                drilldown: function(e) {{
                                    var chart = this.chart;
                                    // Remove all other tasks when drilling down
                                    chart.series.forEach(function(series) {{
                                        if (series.name !== e.point.name && !series.options.isDrilldown) {{
                                            series.remove(false);
                                        }}
                                    }});
                                    chart.redraw();
                                }},
                                drillup: function(e) {{
                                    var chart = this.chart;
                                    // Add back the main tasks when drilling up
                                    chart.series.forEach(function(series) {{
                                        if (series.options.isDrilldown) {{
                                            series.remove(false);
                                        }}
                                    }});
                                    chart.redraw();
                                }}
                            }}
                        }}
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """

    # Write the HTML content to the specified file
    with open(file_name, 'w') as file:
        file.write(html_template)

    print(f"HTML file created: {file_name}")

# Example data passed as input (replace this with your actual data)
tasks = [
    {"name": "Task 1", "start": to_timestamp(dt.date(2023, 1, 1)), "end": to_timestamp(dt.date(2023, 1, 7)), "y": 0, "category": "Design", "drilldown": "task1-subtasks"},
    {"name": "Task 2", "start": to_timestamp(dt.date(2023, 1, 8)), "end": to_timestamp(dt.date(2023, 1, 15)), "y": 1, "category": "Development", "drilldown": "task2-subtasks"},
    {"name": "Task 3", "start": to_timestamp(dt.date(2023, 1, 16)), "end": to_timestamp(dt.date(2023, 1, 23)), "y": 2, "category": "Testing", "drilldown": "task3-subtasks"},
]

# Drilldown data for each task (with parallel subtasks using unique y values for overlapping tasks)
drilldown_tasks = [
    {
        "id": "task1-subtasks",
        "name": "Task 1 Subtasks",
        "data": [
            {"name": "Subtask 1.1", "start": to_timestamp(dt.date(2023, 1, 1)), "end": to_timestamp(dt.date(2023, 1, 2)), "y": 0},  # First subtask
            {"name": "Subtask 1.2", "start": to_timestamp(dt.date(2023, 1, 1)), "end": to_timestamp(dt.date(2023, 1, 3)), "y": 0.1},  # Overlapping subtask with a different y value
            {"name": "Subtask 1.3", "start": to_timestamp(dt.date(2023, 1, 3)), "end": to_timestamp(dt.date(2023, 1, 7)), "y": 0}   # Sequential subtask
        ]
    },
    {
        "id": "task2-subtasks",
        "name": "Task 2 Subtasks",
        "data": [
            {"name": "Subtask 2.1", "start": to_timestamp(dt.date(2023, 1, 8)), "end": to_timestamp(dt.date(2023, 1, 10)), "y": 1},  # Parallel subtask
            {"name": "Subtask 2.2", "start": to_timestamp(dt.date(2023, 1, 8)), "end": to_timestamp(dt.date(2023, 1, 11)), "y": 1.1},  # Overlapping subtask
            {"name": "Subtask 2.3", "start": to_timestamp(dt.date(2023, 1, 11)), "end": to_timestamp(dt.date(2023, 1, 15)), "y": 1}  # Sequential subtask
        ]
    },
    {
        "id": "task3-subtasks",
        "name": "Task 3 Subtasks",
        "data": [
            {"name": "Subtask 3.1", "start": to_timestamp(dt.date(2023, 1, 16)), "end": to_timestamp(dt.date(2023, 1, 18)), "y": 2},  # Parallel subtask
            {"name": "Subtask 3.2", "start": to_timestamp(dt.date(2023, 1, 16)), "end": to_timestamp(dt.date(2023, 1, 20)), "y": 2.1},  # Overlapping subtask
            {"name": "Subtask 3.3", "start": to_timestamp(dt.date(2023, 1, 20)), "end": to_timestamp(dt.date(2023, 1, 23)), "y": 2}   # Sequential subtask
        ]
    },
]

# Generate the HTML file with the Gantt chart and drilldown
create_gantt_chart_html('gantt_chart_with_parallel_subtasks.html', tasks, drilldown_tasks)
