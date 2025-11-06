#import <Foundation/Foundation.h>

#if __has_attribute(swift_private)
#define AC_SWIFT_PRIVATE __attribute__((swift_private))
#else
#define AC_SWIFT_PRIVATE
#endif

/// The "world_map" asset catalog image resource.
static NSString * const ACImageNameWorldMap AC_SWIFT_PRIVATE = @"world_map";

#undef AC_SWIFT_PRIVATE
