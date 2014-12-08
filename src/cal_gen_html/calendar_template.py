from textwrap import dedent

def calendar_month_template():
    return dedent("""\
        <table class='calendar'>
        <thead>
            <tr class='weekdays'>
                <th>Sunday</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
                <th>Saturday</th>
            </tr>
        </thead>
        
        <tbody>
        
        % for week in month.weeks:
        <!-- ${str(week)} -->
        
            <!-- day number band -->
            <tr class='cal_band day_num_band'>
                % for weekday, day in week.enumerate_days():
                    % if day is not None:
                    <th>${day.day_date.day}</th>
                    % else:
                    <th> </th>
                    % endif
                % endfor
            </tr>
            
            <!-- Multi-Day Event Bands -->
            % for band in week.multi_day_bands:
            <tr class='cal_band multi_day_band'>
                % for cell in band.cells:
                <td colspan='${cell.colspan}'>
                
                </td>
                % endfor
            </tr>
            % endfor
            
            
        <!-- end of ${str(week)} -->

        % endfor
        </tbody>
        </table>  <!-- calendar -->
    """)