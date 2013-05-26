//
//  ViewController.h
//  MSClassApp
//
//  Created by Nathan Spaun on 4/12/13.
//  Copyright (c) 2013 BACC. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController {
    NSDate *currentDate;
    BOOL loaded;
}
@property (strong, nonatomic) IBOutlet UITextView *scriptureTextView;
@property (strong, nonatomic) IBOutlet UIImageView *badgeView;
@property (strong, nonatomic) IBOutlet UILabel *dateLabel;
@property (strong, nonatomic) IBOutlet UIButton *tomorrow;

@end
