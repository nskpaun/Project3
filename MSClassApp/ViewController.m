//
//  ViewController.m
//  MSClassApp
//
//  Created by Nathan Spaun on 4/12/13.
//  Copyright (c) 2013 BACC. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    currentDate = [NSDate date];
    [self setViewWithDate];
    // convert it to a string

    
    
	// Do any additional setup after loading the view, typically from a nib.
}



- (NSData *) getDataFrom:(NSString *)url{
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"GET"];
    [request setURL:[NSURL URLWithString:url]];
    
    NSError *error = [[NSError alloc] init];
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    if([responseCode statusCode] != 200){
        NSLog(@"Error getting %@, HTTP status code %i", url, [responseCode statusCode]);
        return nil;
    }
    
    return oResponseData;
}

- (void)setViewWithDate
{
    NSDateFormatter *dateFormat = [[NSDateFormatter alloc]init];
    [dateFormat setDateFormat:@"ddMMYYYY"];
    NSString *dateString = [dateFormat stringFromDate:currentDate];

    NSDictionary *json = [NSJSONSerialization JSONObjectWithData:[self getDataFrom:[NSString stringWithFormat: @"http://sleepy-taiga-5022.herokuapp.com/api/scripture/?date=%@",dateString]] options:nil error:nil];
    NSString *stext = [[json objectForKey:@"scripture"] objectForKey:@"text"];
    NSString *ctext = [[json objectForKey:@"scripture"] objectForKey:@"comment"];
    NSString *rtext = [[json objectForKey:@"scripture"] objectForKey:@"reference"];
    NSString *path = [[json objectForKey:@"scripture"] objectForKey:@"badge_url"];
    
    NSString *questionText = @"Questions";
    
    for( NSDictionary *qJson in [json objectForKey:@"questions"] ) {
        questionText = [NSString stringWithFormat:@"%@\n\n\t%@", questionText, [qJson objectForKey:@"question_text" ]];
    }
    
    NSString *fullText = [NSString stringWithFormat:@"%@\n%@\n\nComments:\n\t%@\n\n%@", rtext,stext,ctext,questionText];
    
    [self.scriptureTextView setText:fullText];
    NSURL *url = [NSURL URLWithString:path];
    NSData *data = [NSData dataWithContentsOfURL:url];
    UIImage *img = [UIImage imageWithData:data];
    
    if ([dateString isEqualToString:[dateFormat stringFromDate: [NSDate date]]]) {
        [self.dateLabel setText:@"Today"];
        [self.tomorrow setHidden:YES];
    } else {
        [dateFormat setDateFormat:@"dd/MM/YYYY"];
        [self.dateLabel setText:[dateFormat stringFromDate:currentDate]];
        [self.tomorrow setHidden:NO];
    }
    
    [self.badgeView setImage: img];
}
- (IBAction)tomorrow:(id)sender {
    NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
    NSDateComponents *todayComponents = [gregorian components:(NSDayCalendarUnit | NSMonthCalendarUnit | NSYearCalendarUnit) fromDate:currentDate];
    NSInteger theDay = [todayComponents day];
    NSInteger theMonth = [todayComponents month];
    NSInteger theYear = [todayComponents year];
    
    // now build a NSDate object for yourDate using these components
    NSDateComponents *components = [[NSDateComponents alloc] init];
    [components setDay:theDay];
    [components setMonth:theMonth];
    [components setYear:theYear];
    NSDate *thisDate = [gregorian dateFromComponents:components];
    
    // now build a NSDate object for the next day
    NSDateComponents *offsetComponents = [[NSDateComponents alloc] init];
    [offsetComponents setDay:1];
    currentDate = [gregorian dateByAddingComponents:offsetComponents toDate:thisDate options:0];
    [self setViewWithDate];
}

- (IBAction)yesterday:(id)sender {
    NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
    NSDateComponents *todayComponents = [gregorian components:(NSDayCalendarUnit | NSMonthCalendarUnit | NSYearCalendarUnit) fromDate:currentDate];
    NSInteger theDay = [todayComponents day];
    NSInteger theMonth = [todayComponents month];
    NSInteger theYear = [todayComponents year];
    
    // now build a NSDate object for yourDate using these components
    NSDateComponents *components = [[NSDateComponents alloc] init];
    [components setDay:theDay];
    [components setMonth:theMonth];
    [components setYear:theYear];
    NSDate *thisDate = [gregorian dateFromComponents:components];
    
    // now build a NSDate object for the next day
    NSDateComponents *offsetComponents = [[NSDateComponents alloc] init];
    [offsetComponents setDay:-1];
    currentDate = [gregorian dateByAddingComponents:offsetComponents toDate:thisDate options:0];
    [self setViewWithDate];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
